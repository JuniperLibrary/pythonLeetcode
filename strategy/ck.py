import clickhouse_driver

client = clickhouse_driver.Client(
    'psbc-middle.internal.quantinfotech.com',
    port=8123,
    user='default',
    password='4J68P9nM',
    database='rates'
)
version = client.execute('SELECT version()')

for row in version:
    print(row[0])

if __name__ == '__main__':

    client = clickhouse_driver.Client(
        'localhost',
        port=8123,
        user='default',
        password='4J68P9nM',
        database='rates'
    )
    print(234+3456)
    version = client.execute('SELECT version()')
    for row in version:
        print(row[0])