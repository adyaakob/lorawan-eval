const functions = require('firebase-functions');
const { spawn } = require('child_process');
const path = require('path');

exports.app = functions.https.onRequest((req, res) => {
  const projectRoot = path.join(__dirname, '..');
  const pythonProcess = spawn('python', [
    path.join(projectRoot, 'wsgi.py')
  ], {
    cwd: projectRoot,
    env: {
      ...process.env,
      PYTHONPATH: projectRoot
    }
  });

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
  });

  // Proxy the request to the Flask app
  req.pipe(pythonProcess.stdin);
  pythonProcess.stdout.pipe(res);
});
