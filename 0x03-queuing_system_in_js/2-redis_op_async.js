import { createClient } from 'redis';


const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value);
  console.log('Reply: OK');
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}

await displaySchoolValue('ALX');
await setNewSchool('ALXSanFrancisco', '100');
await displaySchoolValue('ALXSanFrancisco');

await client.quit();