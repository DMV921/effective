FROM python:3.10-slim
RUN apt-get update && apt-get install -y --no-install-recommends     libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcomposite1     libxrandr2 libasound2 libpangocairo-1.0-0 wget ca-certificates     && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps
COPY . /workspace

CMD ["pytest", "--alluredir=allure-results"]
