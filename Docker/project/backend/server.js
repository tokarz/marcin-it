const express = require('express');
const { Pool } = require('pg');

const app = express();
const pool = new Pool({
  user: 'user',
  host: 'postgres',
  database: 'testdb',
  password: 'password',
  port: 5432,
});

app.get('/', async (req, res) => {
  const result = await pool.query('SELECT NOW()');
  res.send(result.rows);
});

app.listen(3000, () => {
  console.log('Backend listening on port 3000');
});
