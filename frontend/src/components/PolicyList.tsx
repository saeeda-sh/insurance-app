import React, { useEffect, useState } from 'react';
import { getPolicies } from '../api';
import { InsurancePolicy } from '../types';
import { Container, Box, Card, CardContent, Typography, CircularProgress, Alert } from '@mui/material';

const PolicyList: React.FC = () => {
  const [policies, setPolicies] = useState<InsurancePolicy[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const fetchPolicies = async () => {
      try {
        const data = await getPolicies();
        setPolicies(data);
      } catch (error) {
        setError('Failed to fetch policies');
      } finally {
        setLoading(false);
      }
    };

    fetchPolicies();
  }, []);

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Container>
      <Typography variant="h4" gutterBottom align="center" style={{ marginTop: '20px' }}>
        Insurance Policies
      </Typography>
      <Box
        component="div"
        display="flex"
        flexWrap="wrap"
        justifyContent="space-between"
        gap={3}
      >
        {policies.map((policy) => (
          <Box key={policy.policy_id} width="100%" component="div">
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h6" component="div" gutterBottom>
                  {policy.policy_type}
                </Typography>
                <Typography variant="body1" color="text.secondary" style={{ textTransform: 'capitalize' }}>
                  <strong>Status:</strong> {policy.policy_status}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  <strong>Coverage:</strong> ${policy.premium_amount}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  <strong>Start Date:</strong> {new Date(policy.policy_start_date).toLocaleDateString()}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  <strong>End Date:</strong> {new Date(policy.policy_end_date).toLocaleDateString()}
                </Typography>
              </CardContent>
            </Card>
          </Box>
        ))}
      </Box>
    </Container>
  );
};

export default PolicyList;
