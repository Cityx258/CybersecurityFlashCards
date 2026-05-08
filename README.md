# Cybersecurity Flashcards

A terminal-based flashcard study tool for cybersecurity concepts, built for the web4 course.

## Usage

```bash
python3 flashcards.py            # study all cards
python3 flashcards.py <topic>    # filter cards by topic keyword
```

**Examples:**

```bash
python3 flashcards.py cookie     # cookie-related cards only
python3 flashcards.py recon      # reconnaissance cards only
python3 flashcards.py crypto     # cryptography cards only
```

## How it works

Cards are shuffled each session. For each card:

1. The question is displayed — press **Enter** to reveal the answer.
2. Mark yourself **y** (correct), **n** (wrong), or **s** (skip).
3. At the end, you get a score summary.
4. You can replay the same set immediately.

## Topics covered

| Filter keyword | Topic |
|---|---|
| `cookie` | HTTP cookies, PHP `setcookie()`, security flags, session vs persistent |
| `cybersec` | CIA triad, threat/vulnerability/risk, CVE, authentication vs authorization |
| `recon` | Reconnaissance phases, nmap, OSINT, hacker types |
| `crypto` | Hashing, symmetric vs asymmetric encryption, digital signatures |
| `xss` | Cross-site scripting types |
| `dos` | DoS vs DDoS |
| `session` | Web session lifecycle |
| `tls` | TLS handshake |
| `auth` | Authentication factors, MFA |
| `regex` | Regular expressions |

## Adding cards

Edit `flashcards.json` and add an entry:

```json
{
  "id": "unique_id",
  "question": "Your question here?",
  "answer": "Your answer here."
}
```

The `id` field is used for topic filtering — include relevant keywords in it.
