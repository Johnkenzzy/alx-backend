import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Log connection success or failure
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

// const print = redis.print;

// Set hash values
await client.hSet('ALX', 'Portland', 50);
await client.hSet('ALX', 'Seattle', 80);
await client.hSet('ALX', 'New York', 20);
await client.hSet('ALX', 'Bogota', 20);
await client.hSet('ALX', 'Cali', 40);
await client.hSet('ALX', 'Paris', 2);

// Get all hash values
const reply = await client.hGetAll('ALX');
console.log(reply);

await client.quit(); // Close connection