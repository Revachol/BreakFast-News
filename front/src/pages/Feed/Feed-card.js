import React from 'react';
import { Card, CardContent, CardMedia, Typography, Grid, Box } from '@mui/material';

// Feed Item Component
function FeedItem({ item }) {
  return (
    <Grid item xs={12} sm={6} md={4} lg={3}>
      <Card sx={{ minHeight: 150, maxWidth: 300, marginBottom: 2 }}>
        {item.imageUrl && (
          <CardMedia
            component="img"
            style={{ height: '80px', objectFit: 'cover', width: '100%' }}
            image={item.imageUrl}
            alt={item.title}
          />
        )}
        <CardContent sx={{ flexGrow: 1 }}>
          <Typography gutterBottom variant="h6" component="div">
            {item.title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {item.content}
          </Typography>
        </CardContent>
      </Card>
    </Grid>
  );
}

// Feed Component
function Feed() {
  const feedData = [
    {
      title: 'Post 1',
      content: 'Short content 1',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 2',
      content: 'Short content 2',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 3',
      content: 'Short content 3',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 4',
      content: 'Short content 4',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 5',
      content: 'Short content 5',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 6',
      content: 'Short content 6',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 7',
      content: 'Short content 7',
      imageUrl: 'https://via.placeholder.com/150',
    },
    {
      title: 'Post 8',
      content: 'Short content 8',
      imageUrl: 'https://via.placeholder.com/150',
    },
  ];

  return (
    <Grid container spacing={2}>
      {feedData.map((item, index) => (
        <FeedItem key={index} item={item} />
      ))}
    </Grid>
  );
}

export default Feed;
