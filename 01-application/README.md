Команды для пуша образа в docker hub в приватный registry
docker tag echo-server:latest tokyombappy/test
docker login
docker push tokyombappy/test
