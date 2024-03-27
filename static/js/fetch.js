async function fetchApi(url, method = "GET", data = null, headers = {}) {
  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`请检查你的网络或服务器连接: ${response.status}`);
    }
    const res = await response.json();
    if (res.code == 0) {
      return res;
    } else {
      throw new Error(res.message);
    }
  } catch (error) {
    throw new Error(error.message);
  }
}
