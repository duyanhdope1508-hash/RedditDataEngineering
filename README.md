# Personal Reddit Analytics Pipeline

Day la phien ban tuy bien cua du an Reddit data pipeline. Muc tieu cua du an la thu thap bai viet tu Reddit, chuan hoa du lieu thanh CSV, va dua raw data len Amazon S3 de tiep tuc phan tich bang cac dich vu AWS nhu Glue, Athena hoac Redshift.

## Diem khac so voi ban goc

- Doi ten DAG thanh `personal_reddit_analytics_pipeline`.
- Dua subreddit, time filter, limit va user agent vao file config thay vi hard-code trong DAG.
- Bo sung cac cot Reddit huu ich: `upvote_ratio`, `subreddit`, `permalink`.
- Tao thu muc output tu dong truoc khi ghi CSV.
- Xu ly du lieu rong va cot `edited` on dinh hon.
- Viet lai README theo huong ca nhan de de thuyet trinh/bao cao.

## Kien truc

1. Reddit API cung cap du lieu bai viet.
2. Airflow dieu phoi workflow ETL hang ngay.
3. Python/Pandas lam sach va chuan hoa du lieu.
4. Local CSV luu ban raw da chuan hoa.
5. Amazon S3 luu tru file trong folder `raw/`.

## Cau truc thu muc

```text
.
|-- assets/
|-- config/
|   `-- config.conf.example
|-- dags/
|   `-- reddit_dag.py
|-- data/
|   `-- output/
|-- etls/
|   |-- aws_etl.py
|   `-- reddit_etl.py
|-- pipelines/
|   |-- aws_s3_pipeline.py
|   `-- reddit_pipeline.py
|-- utils/
|   `-- constants.py
|-- docker-compose.yml
|-- Dockerfile
`-- requirements.txt
```

## Chuan bi

- Docker va Docker Compose.
- Python 3.9+ neu muon chay local.
- Reddit API credentials.
- AWS access key co quyen tao bucket va upload object len S3.

## Cau hinh

Tao file config rieng tu file mau:

```bash
cp config/config.conf.example config/config.conf
```

Sau do dien cac gia tri:

- `reddit_client_id`
- `reddit_secret_key`
- `aws_access_key_id`
- `aws_secret_access_key`
- `aws_region`
- `aws_bucket_name`

Co the doi phan `[reddit]` de chon subreddit khac:

```ini
[reddit]
subreddit = dataengineering
time_filter = day
post_limit = 100
user_agent = PersonalRedditAnalytics/1.0
```

## Chay voi Docker

Khoi tao database va user Airflow:

```bash
docker-compose up airflow-init
```

Chay cac service:

```bash
docker-compose up -d
```

Mo Airflow UI tai:

```text
http://localhost:8080
```

Tai khoan mac dinh:

```text
username: admin
password: admin
```

Bat DAG `personal_reddit_analytics_pipeline` de chay pipeline.

## Du lieu dau ra

File CSV se duoc tao trong:

```text
data/output/reddit_<YYYYMMDD>.csv
```

Sau do file duoc upload len S3:

```text
s3://<bucket-name>/raw/reddit_<YYYYMMDD>.csv
```

## Huong phat trien tiep

- Them Glue crawler de catalog du lieu S3.
- Tao bang Athena tren folder `raw/`.
- Them job transform sang parquet trong folder `processed/`.
- Nap du lieu da transform vao Redshift.
