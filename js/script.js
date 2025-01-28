const express = require('express');
const fetch = require('node-fetch');
const app = express();

const GITHUB_TOKEN = process.env.GITHUB_TOKEN; // Store the token in an environment variable

app.get('/api/user', async (req, res) => {
  try {
    const response = await fetch('https://api.github.com/user', {
      headers: {
        Authorization: `token ${GITHUB_TOKEN}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user info');
    }

    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
