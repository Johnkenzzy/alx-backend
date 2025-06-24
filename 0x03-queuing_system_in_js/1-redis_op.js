import redis from 'redis';

const client = redis.createClient();

client.on("error", (err) => console.log("Redis Client Error", err.message));
client.on("connect", () => console.log("Redis client connected to the server"));

// Set a new value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Get and display a value from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error("Error fetching value:", err);
    } else {
      console.log(reply);
    }
  });
}

// Connect to Redis and perform operations
client.connect().then(() => {
  displaySchoolValue('ALX');
  setNewSchool('ALXSanFrancisco', '100');
  displaySchoolValue('ALXSanFrancisco');
})
