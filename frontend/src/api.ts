import axios from 'axios';

const API_URL = 'http://localhost:8000/api/policies';

export const getPolicies = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error("Error fetching policies:", error);
    throw error;
  }
};

export const getPolicyById = async (policyId: string) => {
  try {
    const response = await axios.get(`${API_URL}/${policyId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching policy with id ${policyId}:`, error);
    throw error;
  }
};
