# Snippets API

> Version v1

Test description

## Path Table

| Method | Path | Description |
| --- | --- | --- |
| GET | [/notification/](#getnotification) |  |
| POST | [/notification/](#postnotification) |  |
| GET | [/notification/{id}/](#getnotificationid) |  |
| PUT | [/notification/{id}/](#putnotificationid) |  |
| PATCH | [/notification/{id}/](#patchnotificationid) |  |
| DELETE | [/notification/{id}/](#deletenotificationid) |  |
| GET | [/notificationlog/](#getnotificationlog) |  |
| GET | [/project/](#getproject) |  |
| POST | [/project/](#postproject) |  |
| GET | [/project/{id}/](#getprojectid) |  |
| PUT | [/project/{id}/](#putprojectid) |  |
| PATCH | [/project/{id}/](#patchprojectid) |  |
| DELETE | [/project/{id}/](#deleteprojectid) |  |
| POST | [/signin](#postsignin) |  |
| POST | [/signup](#postsignup) |  |
| GET | [/target/](#gettarget) |  |
| POST | [/target/](#posttarget) |  |
| DELETE | [/target/{id}/](#deletetargetid) |  |
| GET | [/template/](#gettemplate) |  |

## Reference Table

| Name | Path | Description |
| --- | --- | --- |
| Notification | [#/components/requestBodies/Notification](#componentsrequestbodiesnotification) |  |
| Project | [#/components/requestBodies/Project](#componentsrequestbodiesproject) |  |
| Basic | [#/components/securitySchemes/Basic](#componentssecurityschemesbasic) |  |
| Notification | [#/components/schemas/Notification](#componentsschemasnotification) |  |
| NotificationLog | [#/components/schemas/NotificationLog](#componentsschemasnotificationlog) |  |
| Project | [#/components/schemas/Project](#componentsschemasproject) |  |
| SignIn | [#/components/schemas/SignIn](#componentsschemassignin) |  |
| SignUp | [#/components/schemas/SignUp](#componentsschemassignup) |  |
| Target | [#/components/schemas/Target](#componentsschemastarget) |  |
| Template | [#/components/schemas/Template](#componentsschemastemplate) |  |

## Path Details

***

### [GET]/notification/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}[]
```

***

### [POST]/notification/

#### RequestBody

- application/json

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

***

### [GET]/notification/{id}/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

***

### [PUT]/notification/{id}/

#### RequestBody

- application/json

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

***

### [PATCH]/notification/{id}/

#### RequestBody

- application/json

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

***

### [DELETE]/notification/{id}/

#### Responses

- 204 

***

### [GET]/notificationlog/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  status: string
  request: {
  }
  response: {
  }
  created_at?: string
  updated_at?: string
  reservation: integer
  target: integer
}[]
```

***

### [GET]/project/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}[]
```

***

### [POST]/project/

#### RequestBody

- application/json

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

***

### [GET]/project/{id}/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

***

### [PUT]/project/{id}/

#### RequestBody

- application/json

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

***

### [PATCH]/project/{id}/

#### RequestBody

- application/json

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

***

### [DELETE]/project/{id}/

#### Responses

- 204 

***

### [POST]/signin

#### RequestBody

- application/json

```ts
{
  email: string
  password: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  email: string
  password: string
}
```

***

### [POST]/signup

#### RequestBody

- application/json

```ts
{
  email: string
  password: string
  username: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  email: string
  password: string
  username: string
}
```

***

### [GET]/target/

#### Responses

- 200 

`application/json`

```ts
{
}[]
```

***

### [POST]/target/

#### RequestBody

- application/json

```ts
{
}
```

#### Responses

- 201 

`application/json`

```ts
{
}
```

***

### [DELETE]/target/{id}/

#### Responses

- 204 

***

### [GET]/template/

#### Responses

- 200 

`application/json`

```ts
{
  id?: integer
  title: string
  content: string
  created_at?: string
  updated_at?: string
}[]
```

## References

### #/components/requestBodies/Notification

- application/json

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

### #/components/requestBodies/Project

- application/json

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

### #/components/securitySchemes/Basic

```ts
{
  "type": "http",
  "scheme": "basic"
}
```

### #/components/schemas/Notification

```ts
{
  id?: integer
  reserved_at: string
  status: string
  type: string
  created_at?: string
  updated_at?: string
  message: integer
  project: integer
}
```

### #/components/schemas/NotificationLog

```ts
{
  id?: integer
  status: string
  request: {
  }
  response: {
  }
  created_at?: string
  updated_at?: string
  reservation: integer
  target: integer
}
```

### #/components/schemas/Project

```ts
{
  id?: integer
  name: string
  project_type: string
  created_at?: string
  updated_at?: string
  user: integer
}
```

### #/components/schemas/SignIn

```ts
{
  email: string
  password: string
}
```

### #/components/schemas/SignUp

```ts
{
  email: string
  password: string
  username: string
}
```

### #/components/schemas/Target

```ts
{
}
```

### #/components/schemas/Template

```ts
{
  id?: integer
  title: string
  content: string
  created_at?: string
  updated_at?: string
}
```
