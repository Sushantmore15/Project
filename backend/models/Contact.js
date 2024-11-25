const db = require('../db');

// Contact Model
const Contact = {
  create: (name, email, message, callback) => {
    const query = 'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)';
    db.query(query, [name, email, message], callback);
  },
};

module.exports = Contact;
