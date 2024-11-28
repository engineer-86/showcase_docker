## 1. **Build Server Container**
### Dockerfile

### Build Command
```bash
docker build -f Dockerfile.server -t myserver:latest .
```

### Run Command
```bash
docker run -d --name server-container -p 5000:5000 myserver:latest
```

---

## 2. **Build Client Container**
### Dockerfile

### Build Command
```bash
docker build -f Dockerfile.client -t myclient:latest .
```

### Run Command
```bash
docker run -d --name client-container --link server-container myclient:latest
```

---

## 3. **Check Running Containers**
```bash
docker ps
```

---

## 4. **Stopping Containers**

```bash
docker stop server-container server-container

docker stop server-container client-container
```

---

## 5. **Remove Containers**

```bash
docker rm server-container server-container

docker rm server-container client-container
```

---

## 6. **Optional: Remove Images**

```bash
docker rmi myserver:latest myclient:latest
```

---

