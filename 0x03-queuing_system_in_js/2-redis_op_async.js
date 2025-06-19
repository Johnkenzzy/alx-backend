import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = createClient();

// Log connection status
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

// Function to set a value (unchanged)
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

// Function to get a value using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error getting key ${schoolName}:`, err);
  }
}

// Perform operations
(async () => {
  await displaySchoolValue('ALX');
  setNewSchool('ALXSanFrancisco', '100');
  await displaySchoolValue('ALXSanFrancisco');
})();