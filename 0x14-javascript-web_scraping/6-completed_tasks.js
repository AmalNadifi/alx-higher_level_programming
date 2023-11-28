#!/usr/bin/node

const request = require('request');

// URL from command line arguments
const apiUrl = process.argv[2];

// Count of completed tasks per user
const completedTasksByUser = {};

// Make a GET request to the specified URL
request(apiUrl, (error, response, body) => {
  // Check for errors in the request
  if (!error) {
    // Parse the JSON response
    const tasks = JSON.parse(body);

    // Iterate through tasks
    for (const task of tasks) {
      // Extract user ID
      const userId = task.userId;

      // If task is completed and user ID not in the object, initialize to 0
      if (task.completed && !(userId in completedTasksByUser)) {
        completedTasksByUser[userId] = 0;
      }

      // If task is completed, increment count for the user
      if (task.completed) completedTasksByUser[userId]++;
    }

    // Print the final count of completed tasks per user
    console.log(completedTasksByUser);
  }
});
