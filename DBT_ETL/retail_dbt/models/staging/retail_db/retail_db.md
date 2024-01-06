{% docs order_status %}
	
One of the following values: 

| status         | definition                                       |
|----------------|--------------------------------------------------|
| CLOSED         | Order placed and delivered                       |
| ON_HOLD        | Order is on hold                                 |
| PENDING        | Order is placed, yet to be delivered             |
| CANCELED       | Order is cancelled by user or seller             |
| COMPLETE       | Order has been received by customers             |
| PROCESSING     | Order is placed, payment is processing           |
| PAYMENT_REVIEW | Payment for the order is under review            |
| PENDING_PAYMENT| Payment for the order is pending                 |
| SUSPECTED_FRAUD| Order placed is flagged as fraud                 |

{% enddocs %}