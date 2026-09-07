# Aplicativo de contador com Flutter

Depois de tentar criar esse aplicativo com Kotlin, desisti.

## Build

Instalando:

```{bash}
sudo apt update sudo apt install -y curl git unzip xz-utils zip libglu1-mesa

git clone https://github.com/flutter/flutter.git -b stable ~/flutter

echo 'export PATH="$HOME/flutter/bin:$PATH"' >> ~/.bashrc source ~/.bashrc

flutter --version 
dart --version

#--

flutter doctor
flutter doctor --android-licenses

flutter pub get
```

Rodando:

```{bash}
flutter run

#--

adb devices
flutter devices
flutter run -d devices

#--

flutter build apk --release
```

