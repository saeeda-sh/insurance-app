export interface InsurancePolicy {
  policy_id: string;
  policy_type: string;
  premium_amount: number;
  policy_start_date: string;
  policy_end_date: string;
  policy_status: 'active' | 'expired' | 'canceled' | 'pending';
  customer_id: string;
}

export interface Customer {
  customer_id: string;
  first_name: string;
  last_name: string;
}
