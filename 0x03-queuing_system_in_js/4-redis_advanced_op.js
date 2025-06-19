import { createClient, print } from 'redis';

// Create Redis client
const client = createClient();

// Log connection success or failure
client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Set hash values
  client.hset('ALX', 'Portland', 50, print);
  client.hset('ALX', 'Seattle', 80, print);
  client.hset('ALX', 'New York', 20, print);
  client.hset('ALX', 'Bogota', 20, print);
  client.hset('ALX', 'Cali', 40, print);
  client.hset('ALX', 'Paris', 2, print);

  // Get all hash values
  client.hgetall('ALX', (err, reply) => {
    if (err) {
      console.error('Error fetching hash:', err);
    } else {
      console.log(reply);
    }
  });
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});