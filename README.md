# CryptageSimple

Le chiffrement César simple est une technique de chiffrement par décalage qui a été utilisée depuis des siècles pour protéger des messages confidentiels. Il doit son nom à Jules César, qui aurait utilisé ce chiffrement pour communiquer avec ses généraux.

Le fonctionnement du chiffrement César est assez simple. Chaque lettre du message d'origine est décalée vers la droite d'un certain nombre fixe de positions dans l'alphabet. Par exemple, avec un décalage de 3, la lettre 'A' devient 'D', 'B' devient 'E', et ainsi de suite. Ce décalage est également appelé la clé de chiffrement.

En utilisant l'opérateur modulo (représenté par le symbole `%`), nous pouvons nous assurer que le décalage reste toujours à l'intérieur de la plage valide des indices de l'alphabet. Par exemple, si nous avons un alphabet de 26 lettres, le modulo 26 nous ramènera toujours à un nombre entre 0 et 25.

Voici un exemple de chiffrement César avec un décalage de 3 :

Message d'origine : "HELLO"
Message chiffré : "KHOOR"

Pour décrypter le message chiffré, il suffit d'effectuer le décalage inverse en déplaçant chaque lettre vers la gauche. Par exemple, avec un décalage de 3, la lettre 'K' devient 'H', 'H' devient 'E', et ainsi de suite.

Le chiffrement César simple est facile à comprendre et à mettre en œuvre. Cependant, il est considéré comme un chiffrement très faible, car il est vulnérable aux attaques par force brute et aux analyses fréquentielles.
