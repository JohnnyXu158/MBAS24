# MBAS 2024 (MICCAI MBAS 2024 - Multi-class Bi-Atrial Segmentation Challenge)

> ⚠️ **IMPORTANT NOTICE: LICENSE AND MANDATORY CITATION REQUIREMENTS**
> Please read the following terms carefully before downloading or using any contents of this repository. By using this data, you agree to these terms.

### 📜 License & Usage Restrictions
We are open to the data being used to test AI approaches; however, **the use of the data and labels for commercialization or other purposes is strictly prohibited.** Any other uses require contacting the team to obtain written permission.

### 📝 Mandatory Citation Policy
The official paper associated with this dataset is currently pending publication. However, **citation is strictly mandatory**. 
Once the paper is officially published and the citation details are updated in this repository, **anyone using this data for training, testing, or publishing articles MUST include the correct citation.** 
Failure to provide the proper citation constitutes a severe violation of our terms of use. The authors and organizers hold no responsibility or liability for any academic, legal, or other consequences arising from such violations.

*(Note: Please check back regularly. The BibTeX citation will be provided here as soon as the paper is published.)*

---

## Overview

This repository contains the dataset splits, pre-processed data, source code, and model checkpoints for our solution to the MBAS 2024 (Multi-class Bi-Atrial Segmentation) Challenge, held in conjunction with MICCAI 2024.

The MBAS 2024 challenge focuses on the automatic semantic segmentation of bi-atrial anatomical structures (both the left and right atria, along with their walls) using 3D Late Gadolinium-Enhanced Magnetic Resonance Imaging (LGE-MRI). Accurate segmentation of these structures is a crucial preliminary step for clinical evaluation and patient-specific ablation treatments for Atrial Fibrillation (AF).

## Contents of this Repository

* **Training & Testing Data**: Training data consist of 70 raw labels mapped to five semantic classes: 0—background (BAK), 1—right atrium (RA), 2—left atrium (LA), 3—right atrial wall (RAW), and 4—left atrial wall (LAW). Test data consist of 30 raw labels mapped to five semantic classes: 0—background (BAK), 1—right atrium (RA), 2—left atrium (LA), 3—right atrial wall (RAW), and 4—left atrial wall (LAW).
* **Framework Source Code**: Complete deep learning pipelines detailing our data preprocessing, model training, cross-validation, and inference procedures. *(Coming soon on GitHub)*

## Links & References

* **Official MBAS 2024 Challenge Page**: [MBAS24](https://codalab.lisn.upsaclay.fr/competitions/18516) 
* **Download Link**: [MBAS24 Dataset](https://zenodo.org/records/19120533)
* **Associated Paper/Report**: **TBD** *(Will be updated soon. Please refer to the Mandatory Citation Policy above).*

## Acknowledgments

We sincerely thank the multiple institutions that generously provided the data for this challenge. We also extend our deepest gratitude to all of our team members for their hard work, dedication, and support throughout the competition.
