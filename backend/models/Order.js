const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  products: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Product' }],
  status: { type: String, enum: ['pending', 'shipped', 'delivered'], default: 'pending' },
  paymentInfo: {
    method: String,
    amount: Number,
    transactionId: String,
  },
});

module.exports = mongoose.model('Order', orderSchema);
