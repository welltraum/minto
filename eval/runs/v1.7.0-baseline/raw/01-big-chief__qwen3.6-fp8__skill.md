Subject: Accept Big Chief Monthly Settlement Request Subject to Conditions

Big Chief has requested to replace individual ticket settlements with a monthly electronic file and a single payment. Finance has reviewed the proposal and determined that implementation requires adherence to specific data standards, a defined submission workflow, and strict balancing controls. Accordingly, we can accept the request provided the following conditions are met.

1. Data Requirements
- The external account file must contain the parent number, outlet number, ticket number, ticket amount, and delivery date.
- If Big Chief cannot provide the parent or outlet numbers, we will supply these identifiers from the customer master file for inclusion in later submissions.

2. Submission and Balancing Procedures
- Big Chief must build an extraction program for its accounts-payable file.
- The resulting file must use the format accepted by our national-accounts cash-receipt system.
- Big Chief will send the file to Data Processing and deliver the cheque with a detailed listing to the lockbox.
- We will balance the file under the prescribed procedure, ensuring the cheque total and file detail net to zero.

3. System Processing and Billing
- Once balanced, the monthly file will run through the national-accounts system.
- The system will match ticket numbers against statement history and produce the relevant billing records.

```mermaid
flowchart TD
    A["Accept Big Chief Monthly Settlement\nSubject to Conditions"] --> B1["Data Requirements"]
    A --> B2["Submission & Balancing"]
    A --> B3["System Processing"]
    B1 --> C11["Include parent, outlet, ticket,\namount, and date"]
    B1 --> C12["Supply missing parent/outlet\nIDs from master file"]
    B2 --> C21["Build extraction program\nfor AP file"]
    B2 --> C22["Use format accepted by\ncash-receipt system"]
    B2 --> C23["Send file to Data Processing;\nCheque + listing to lockbox"]
    B2 --> C24["Balance file per procedure;\nTotal and detail net to zero"]
    B3 --> C31["Run balanced file through\nnational-accounts system"]
    B3 --> C32["Match ticket numbers against\nstatement history"]
    B3 --> C33["Produce relevant billing records"]
```
