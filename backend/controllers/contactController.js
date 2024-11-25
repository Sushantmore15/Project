const db = require('../db');

// Handle Contact Form Submission
exports.submitContactForm = (req, res) => {
  const { name, email, message } = req.body;

  db.query(
    'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
    [name, email, message],
    (err, result) => {
      if (err) return res.status(500).json({ message: 'Database error', err });
      res.status(201).json({ message: 'Contact form submitted successfully!' });
    }
  );
};
