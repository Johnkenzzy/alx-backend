import { createClient } from 'redis';

// Create Redis client
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Subscribe to ALX channel
client.subscribe('ALX channel', (err) => {
  if (err) {
    console.error('Subscription failed:', err);
  }
});

// Handle incoming messages
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
