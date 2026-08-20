Subject: Big Chief monthly settlement implementation

Big Chief has requested to replace individual ticket settlement with a monthly computer file and one payment. Finance reviewed the proposal and determined the data, submission, and processing steps required to execute it. We can implement this request by meeting the following requirements:

**File content**
The external account file must include the parent number, outlet number, ticket number, ticket amount, and delivery date. If Big Chief cannot provide the parent and outlet numbers, we will supply these identifiers from the customer master file for inclusion in subsequent submissions.

**Submission and balancing**
Big Chief must develop an extraction program for its accounts-payable file using a format compatible with our national-accounts cash-receipt system. They will transmit the file to Data Processing and deliver the cheque along with a detailed listing to the lockbox. We will balance the file according to the prescribed procedure, verifying that the cheque total and file detail net to zero.

**Post-processing**
After balancing, the monthly file will run through the national-accounts system to match ticket numbers against statement history and generate the corresponding billing records.

---

Top: We can implement Big Chief's monthly settlement request by requiring a compliant file format, specific data fields including parent and outlet numbers, and a balancing procedure where the cheque nets to zero.
  1. File content requirements
     - Must contain parent number, outlet number, ticket number, ticket amount, and delivery date.
     - If parent and outlet numbers are missing, we supply them from the customer master file.
  2. Submission and balancing procedures
     - Big Chief builds extraction program using format accepted by national-accounts cash-receipt system.
     - Big Chief sends file to Data Processing and cheque with listing to lockbox.
     - We balance file; cheque total and file detail must net to zero.
  3. Post-processing system actions
     - Balanced file runs through national-accounts system.
     - System matches ticket numbers against statement history.
     - System produces relevant billing records.
