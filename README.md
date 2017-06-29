- settings 분리

```
(deploy_ec2_env) ➜  settings git:(master) ✗ tree
.
├── __init__.py
├── __pycache__
│   ├── __init__.py
│   ├── base.py
│   └── debug.py
├── base.py
└── debug.py
```

- config_secret / setting_OOO.json 으로 Repository에 올라가면 안되는 키값 별도 셋팅