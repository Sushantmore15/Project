const express = require('express');
const router = express.Router();
const Product = require('../models/Product');
const protectRoute = require('../middlewares/authMiddleware');

// Add a new product
router.post('/products', protectRoute, (req, res) => {
  const { name, description, price, category } = req.body;
  const newProduct = new Product({ name, description, price, category, sellerId: req.user.id });
  newProduct.save()
    .then(product => res.json(product))
    .catch(err => res.status(400).json({ error: err.message }));
});

// Get all products for seller
router.get('/products', protectRoute, (req, res) => {
  Product.find({ sellerId: req.user.id })
    .then(products => res.json(products))
    .catch(err => res.status(400).json({ error: err.message }));
});

module.exports = router;
