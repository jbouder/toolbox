# Find and Kill Process
lsof -i tcp:8000
kill -9 12345

# Stop all Docker containers matching a name
docker container stop $(docker container ls -q --filter name=code-migration-test-env)  
