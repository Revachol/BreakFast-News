import React from 'react';
import { Card, CardContent, CardMedia, Typography, Grid, Box } from '@mui/material';

// Feed Item Component
function FeedItem({ item }) {
  return (
    <Box sx={{ width: 700, mx: 'auto', marginBottom: 2 }}> {/* mx: 'auto' centers horizontally */}
      <Card sx={{ minHeight: 150, maxWidth: 700 }}> {/* maxWidth also set to 700 */}
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
    </Box>
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
    <Box>
      {feedData.map((item, index) => (
        <FeedItem key={index} item={item} />
      ))}
    </Box>
  );
}

export default Feed;
