Start server:


```
poetry run python server.py
```

This subscription request works OK in graphiql:

```
subscription Count {
  count(target: 10)
}
```

This script fails to run:

```
poetry run python client.py
```

Stack trace:

```
▶ poetry run python client.py
Traceback (most recent call last):
  File "/home/mike/code/reproduction-gql-subscription-issue/client.py", line 19, in <module>
    for result in client.subscribe(query):
  File "/home/mike/.cache/pypoetry/virtualenvs/reproduction-gql-subscription-issue-t7IDVnbg-py3.11/lib/python3.11/site-packages/gql/client.py", line 600, in subscribe
    loop.run_until_complete(generator_task)
  File "/home/mike/.pyenv/versions/3.11.4/lib/python3.11/asyncio/base_events.py", line 653, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
gql.transport.exceptions.TransportQueryError: {'message': "The subscription field '__schema' is not defined.", 'locations': [{'line': 2, 'column': 3}]}
```
