import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Redis client setup
const client = redis.createClient();
client.on('error', (err) => console.error('Redis client error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Product list
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Utility to get product by ID
const getItemById = (id) => listProducts.find((item) => item.itemId === id);

// Reserve stock in Redis
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Get reserved stock from Redis
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
};

// List all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Get details of a specific product
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = reserved !== null
    ? product.initialAvailableQuantity - reserved
    : product.initialAvailableQuantity;

  res.json({
    ...product,
    currentQuantity,
  });
});

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = reserved !== null
    ? product.initialAvailableQuantity - reserved
    : product.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  const newReserved = reserved !== null ? reserved + 1 : 1;
  await reserveStockById(itemId, newReserved);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});