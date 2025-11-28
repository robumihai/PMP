# Explicatii Laborator 9

## b) Efectul lui Y și Theta
Observăm că distribuția posterioară a lui n (numărul total de clienți) depinde direct de datele observate Y:
- Odată ce Y crește, distribuția lui n se mută către valori mai mari (trebuie să existe cel puțin Y clienți).
- Theta (probabilitatea de cumpărare) acționează invers proporțional: un theta mic implică un n mult mai mare pentru a justifica același număr de cumpărători Y.

## d) Posterior vs Predictive Posterior
- **Posterior (n)**: Reprezintă incertitudinea noastră despre parametrul latent (câți oameni au intrat în magazin în ziua observată).
- **Posterior Predictive (Y*)**: Reprezintă distribuția unor viitoare date observabile (câți oameni ar cumpăra mâine), luând în calcul incertitudinea parametrului n. Aceasta are o varianță mai mare decât posteriorul parametrilor.