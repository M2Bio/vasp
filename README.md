# VASP - Virtual Automated Screening Platform

- Objective: Develop an automated pipeline for molecular docking, starting from a list of compounds to ranking potential leads.
- Skills Learned: Automation (Snakemake, Nextflow), molecular docking tools (AutoDock, PyMOL), and cheminformatics.
- Pharma Relevance: High-throughput virtual screening for drug discovery.

## Next Steps

- [ ] Docker container
- [ ] Snakemake pipeline
  - [ ] AutoDock Vina
- [ ] IO and pre-processing
- [ ] Scoring of docking results

## Test Data

For now, we will use the LIT-PCBA dataset as a test case. The dataset is available at [drugdesign.unistra.fr](http://drugdesign.unistra.fr/LIT-PCBA/).

### Download LIT-PCBA

```bash
wget http://drugdesign.unistra.fr/LIT-PCBA/Files/AVE_unbiased.tgz -P lit-pcba && tar -xzf lit-pcba/AVE_unbiased.tgz -C lit-pcba
```
