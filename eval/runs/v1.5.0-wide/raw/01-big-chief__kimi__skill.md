To: Robert Salton
From: John Jackson
Subject: Big Chief request — the proposed process works; recommend acceptance

Big Chief (account 8306) has asked to replace individual delivery-ticket settlement with a monthly electronic file and one prepaid payment. We reviewed the proposal: it fits our national-accounts cash-receipt process, and I recommend we accept it. It runs in three stages:

1. **File setup.** The monthly file must carry the parent number, outlet number, ticket number, ticket amount, and delivery date. If Big Chief cannot supply the first two identifiers, we provide them from the customer master file for inclusion in later submissions.

2. **Submission and balancing.** Big Chief builds an extraction program on its accounts-payable file, producing the format our national-accounts cash-receipt system accepts. It sends the file to Data Processing and the cheque, with a detailed listing, to the lockbox. We balance the file under the prescribed procedure; the cheque total and the file detail must net to zero.

3. **Processing.** Once balanced, the file runs through the national-accounts system, matches ticket numbers against statement history, and produces the relevant billing records.

```mermaid
flowchart TD
    A["Accept Big Chief's request: the proposed process fits our national-accounts system"] --> B1["1. File setup: file carries the five identifiers (we can supply parent/outlet numbers)"]
    A --> B2["2. Submission and balancing: compatible file to DP, cheque to lockbox, net to zero"]
    A --> B3["3. Processing: balanced file matches ticket history, produces billing records"]
    B1 --> C11["Required: parent no., outlet no., ticket no., amount, delivery date"]
    B2 --> C21["Extraction program on Big Chief's AP file; prescribed balancing procedure"]
    B3 --> C31["Match against statement history; generate billing records"]
```
