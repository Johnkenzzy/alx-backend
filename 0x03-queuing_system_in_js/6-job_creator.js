import kue from 'kue';

// Create Kue queue
const queue = kue.createQueue();

// Job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the notification message',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData);

// Save the job and handle events
job
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });