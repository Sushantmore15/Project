const express = require('express');
const router = express.Router();
const User = require('../models/User');
const Order = require('../models/Order');
const protectRoute = require('../middlewares/authMiddleware');

// Get all users (admin only)
router.get('/users', protectRoute, (req, res) => {
  User.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json({ error: err.message }));
});

// Get all orders (admin only)
router.get('/orders', protectRoute, (req, res) => {
  Order.find()
    .then(orders => res.json(orders))
    .catch(err => res.status(400).json({ error: err.message }));
});

module.exports = router;
