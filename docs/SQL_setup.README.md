# Supabase PostgreSQL Database Setup for Virtual Organization

This documentation describes the database setup in **Supabase PostgreSQL** for managing projects, programs, documentation, ISO processes, and integrations with external systems like GitHub, Docker, Dropbox, and ClickUp.

## Tables

### **programmer** - Overview of programs used in the organization.
- Fields: `program_id`, `program_navn`, `beskrivelse`, `formål`, `status`, `start_dato`, `slutt_dato`, `ansvarlig_person_id`.

### **ansatte** - Employee information.
- Fields: `person_id`, `fornavn`, `etternavn`, `epost`, `telefonnummer`, `stilling`, `avdeling`, `ansatt_dato`.

### **prosjekter** - Overview of projects in the organization.
- Fields: `prosjekt_id`, `prosjekt_navn`, `beskrivelse`, `start_dato`, `slutt_dato`, `status`, `prosjektleder_id`.

### **dokumentasjon** - Documentation related to ISO processes and projects.
- Fields: `dokument_id`, `dokument_navn`, `dokument_type`, `opplastet_dato`, `versjon`, `filbane`, `relatert_prosjekt_id`, `ansvarlig_person_id`.

### **prosesser** - ISO-related processes.
- Fields: `prosess_id`, `prosess_navn`, `beskrivelse`, `prosess_status`, `ansvarlig_person_id`, `sist_oppdatert`.

### **integrasjoner** - Integration information for external systems (GitHub, Docker, Dropbox, ClickUp).
- Fields: `integrasjon_id`, `system_navn`, `api_nokkel`, `status`, `beskrivelse`, `sist_synkronisert`, `relatert_program_id`.

## Views

### **programmer_prosjekter_view**
Combines program and project information.
```sql
CREATE VIEW programmer_prosjekter_view AS
SELECT 
    prog.program_navn,
    prog.beskrivelse AS program_beskrivelse,
    p.prosjekt_navn,
    p.start_dato,
    p.slutt_dato
FROM programmer prog
JOIN program_prosjekt pp ON prog.program_id = pp.program_id
JOIN prosjekter p ON pp.prosjekt_id = p.prosjekt_id;
CREATE VIEW prosjekt_dokumentasjon_view AS
SELECT 
    p.prosjekt_id,
    p.prosjekt_navn,
    d.dokument_navn,
    d.dokument_type,
    d.opplastet_dato,
    d.versjon
FROM prosjekter p
JOIN prosjekt_dokumentasjon pd ON p.prosjekt_id = pd.prosjekt_id
JOIN dokumentasjon d ON pd.dokument_id = d.dokument_id;
CREATE INDEX idx_prosjekter_status ON prosjekter(status);

---

### Hvordan Lagre i **GitHub**:
1. Opprett et nytt repository på GitHub (eller bruk et eksisterende).
2. Lag en ny fil kalt `README.md` og lim inn GitHub-dokumentasjonen over.
3. Lagre og push filen til ditt repository.

### Hvordan Lagre i **Word**:
1. Kopier innholdet fra **Word-dokumentasjon**-delen.
2. Åpne et nytt Word-dokument og lim inn innholdet.
3. Lagre dokumentet som `.docx` eller `.pdf` etter behov.

---

Er dette tilstrekkelig struktur for dokumentasjonen? Jeg kan hjelpe med mer spesifik informasjon eller tilpasninger dersom det er nødvendig.
