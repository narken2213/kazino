from requests import get, post

print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
            json={'job': 'Заголовок'}).json())

#неправильный запрос
print(post('http://localhost:5000/api/jobs',
            json={'team_leader': 't'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок',
                 'team_leader': 1,
                 'work_size': 1}).json())

print(get('http://localhost:5000/api/jobs').json())