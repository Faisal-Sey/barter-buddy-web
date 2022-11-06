# Amalitech Hackathon 2022 | README Guide
![Amalitech](amalitech.jpeg)

# Project Description
A community based to connect buddies to share skills

## Tech Stack

**Client:** HTML, CSS, JavaScript, Tailwind

**Server:** Python

## Features
1. Local Authentication | email and password
2. OAuth 2.0 | Google, Facebook, Twitter
3. File Upload management
4. Payment management | Stripe, Mobile Money 
5. Email Notification 
6. Contact Form | mailgun, Sendgrid


# Preview
- [projectname](https://projectname)

This section should include any type of preview elements that would give an insight into what your 
submission loks like. It can be GIFs, images, videos, or anything similar.


# Project Setup
This section should cover how to set up and run the project locally.

## Prerequisites
If running your submission requires any prerequisites, make sure to list them in this section.
- Nodejs v14
- Postgres

## Install Project
1. Clone the repository:
```sh
git clone https://github.com/
```
2. Change directory
```sh
cd my-project
```
3. Install dependencies
```sh
npm install
```
4. Start server
```sh
npm run start
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

`DB_NAME`

# API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Lessons Learned

1. What did you learn while building this project? 
2. What challenges did you face and how did you overcome them?

# Participants
- [@CyrilBaah](https://www.github.com/CyrilBaah) | DevOps

