Bien sûr, voici votre texte corrigé avec quelques améliorations :

Étape 1 : Télécharger Python 3.12.0

Téléchargez Python 3.12.0 à partir du site officiel de Python. Lors de l'installation, assurez-vous de cocher l'option "Add python.exe to PATH" (Ajouter python.exe au PATH) pour pouvoir accéder à Python plus facilement.

Étape 2 : Ouvrir PowerShell et Accéder au Dossier

Une fois Python installé, ouvrez PowerShell en appuyant sur Win + R, puis en tapant "powershell". Ensuite, accédez au dossier où vous avez placé votre script. Par exemple, si votre script est sur le bureau, utilisez la commande cd dans PowerShell comme ceci : cd C:\Users\{votre_nom}\Desktop\Bypass-script

Étape 3 : Installer les Dépendances

Maintenant que vous êtes dans le bon dossier, installez les dépendances en utilisant la commande suivante : pip install -r requirements.txt

Suivez les instructions qui apparaissent.

Étape 4 : Configuration du ChromeDriver

Placez le fichier chromedriver.exe dans le dossier "C:\Program Files (x86)". C'est crucial pour le bon fonctionnement du script. Assurez-vous d'avoir Google Chrome installé, avec une version égale ou supérieure à "118.0.5993.70". Vous pouvez vérifier la version en cliquant sur les trois petits points en haut à droite, puis en sélectionnant "Aide" -> "À propos de Google Chrome".

Étape 5 : Exécuter le Script

Vous avez maintenant tout installé correctement ! Vous pouvez lancer le script "script_bypass.py" en le double-cliquant. Suivez les instructions pour entrer votre Identifiant et Mot de passe pour vous connecter au site web de Gloria. Le code source est à votre disposition pour inspection en ouvrant le fichier "script_bypass.py" avec un éditeur de texte quelconque.

Une fois les identifiants saisis, le script fonctionnera automatiquement toutes les 1h30 et votera à votre place, même si vous êtes en train de dormir.

Vous êtes prêt à voter en toute simplicité 24/7 ! 😄 Cela fait environ 18 votes par jour, pas mal, non ?

POTENTIELS PROBLÈMES :

Si le script ne vote pas correctement, vérifiez s'il y a une image ou plusieurs images dans le dossier qui s'est créé en dehors des dossiers "[1, 2, 3, 4, 5, 6, 7, 8, 9]". Si une image se trouve là, ouvrez l'image et regardez le chiffre du captcha. Placez le chiffre du captcha dans le dossier correspondant. Par exemple, si l'image du captcha est "3", mettez l'image dans le dossier "3".

Il peut arriver que le site de vote mette à jour leur base de données et ajoute de nouvelles images de captcha ou enlève d'anciennes. Pas de souci, j'y ai pensé. Le script "taking_images.py" permet de télécharger en boucle toutes les nouvelles images. Si l'image existe déjà, nous ne la conservons pas. Donc, si vous voyez que votre script télécharge plusieurs images mais que le vote ne fonctionne pas, lancez le script et attendez une bonne nuit de repos (7 à 8 heures devraient suffire) pour télécharger toutes les nouvelles images du site. Ensuite, vous devrez trier les images dans les dossiers correspondants, et le script fonctionnera à nouveau.

Si vous avez des questions ou si le script ne fonctionne pas pour une raison quelconque, venez me contacter sur Discord, je vous répondrai dès que possible. Mon pseudo Discord est "mrpropreuh".

Vous pouvez inviter vos amis à venir me voir pour acheter la macro.

TOS (Conditions d'utilisation) :

PS : Pas de remboursement, cela peut sembler évident, car si Gloria change sa méthode de vote, le script ne fonctionnera plus. Mais ne vous inquiétez pas, cela ne devrait probablement pas arriver. Bon jeu !

Je ne suis pas responsable d'un éventuel bannissement. Trop de votes en peu de temps et atteindre la première place en quelques jours pourrait éveiller des soupçons. Assurez-vous de voter de manière raisonnable pour éviter tout problème.