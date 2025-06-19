import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to set value for a key
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // redis.print logs: Reply: OK
}

// Function to display value of a key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    console.log(reply);
  });
}

// Test the functions
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');