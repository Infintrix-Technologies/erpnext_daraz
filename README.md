# Daraz Integration for ERPNext

This app enables seamless integration between [Daraz](https://www.daraz.pk/) and [ERPNext](https://erpnext.com/), allowing businesses to streamline their operations by syncing orders, inventory, and other data across platforms.

## Features
- **Order Synchronization**: Automatically fetch orders from Daraz and update them in ERPNext.
- **Inventory Sync**: Sync product stock levels between ERPNext and Daraz.
- **Product Mapping**: Link Daraz products with ERPNext items for efficient tracking.
- **Status Updates**: Push order status updates from ERPNext to Daraz.
- **Custom Reports**: Generate detailed reports on sales and inventory performance.

## Prerequisites
- ERPNext v14 or higher
- Frappe framework installed
- Daraz seller account with API access

## Installation

1. Install the app:
   ```bash
   bench get-app https://github.dev/Infintrix-Technologies/erpnext_daraz.git
   bench install-app daraz_integration
   ```
2. Configure your Daraz API credentials:
   - Go to the Daraz Integration settings in ERPNext.
   - Enter your `API Key`, `API Secret`, and other required details.

3. Set up scheduler events for periodic synchronization:
   ```bash
   bench --site [sitename] enable-scheduler
   ```

## Configuration

### Setting Up API Credentials
1. Log in to your Daraz seller account.
2. Navigate to the API settings and obtain your API key and secret.
3. In ERPNext:
   - Go to **Daraz Integration > Settings**.
   - Enter the API credentials and save.

### Scheduler Events
Ensure the following scheduler events are enabled:
- Sync Orders: Runs periodically to fetch new orders from Daraz.
- Sync Inventory: Updates stock levels between ERPNext and Daraz.

### Product Mapping
Link ERPNext items to Daraz products using the **Product Mapping** tool under **Daraz Integration**.

## Service Endpoints

| Region      | Endpoint                                |
|-------------|----------------------------------------|
| Pakistan    | https://api.daraz.pk/rest              |

## Usage
- **Order Sync**: Automatically or manually sync orders from Daraz to ERPNext under **Daraz Integration > Order Sync**.
- **Inventory Management**: Use the **Sync Inventory** button to ensure stock levels are consistent across platforms.
- **Custom Reports**: Navigate to **Reports > Daraz Reports** for sales and inventory insights.

## Troubleshooting
- **Invalid API Credentials**: Double-check your API key and secret in the Daraz settings.
- **Scheduler Not Running**: Ensure the site scheduler is enabled and active.
- **Sync Issues**: Check logs under **Error Logs** in ERPNext for detailed error messages.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Need Help?
Feel free to create an issue in this repository or contact our support team.

#### License

MIT