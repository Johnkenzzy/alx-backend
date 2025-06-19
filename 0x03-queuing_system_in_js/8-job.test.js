import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Setup test mode
  before(() => {
    queue = kue.createQueue();
    kue.Job.rangeByType('push_notification_code_3', 'active', 0, -1, 'asc', () => {}); // prevent warnings
    queue.testMode.enter();
  });

  // Cleanup after tests
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '0987654321',
        message: 'This is the code 4321 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    jobs.forEach((job, index) => {
      const testJob = queue.testMode.jobs[index];
      expect(testJob.type).to.equal('push_notification_code_3');
      expect(testJob.data).to.deep.equal(job);
    });
  });
});