# Configurando o Oh-My-Posh no PowerShell

O Oh-My-Posh é um conjunto de temas personalizados para o prompt do PowerShell que permitem que você customize a aparência do seu terminal. Para configurar o Oh-My-Posh, siga os passos abaixo:

## Instalando o Posh-Git e o Oh-My-Posh

Para instalar o Posh-Git e o Oh-My-Posh, execute os seguintes comandos no terminal do PowerShell:

```
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
```

## Configurando o Oh-My-Posh

Para configurar o Oh-My-Posh, insira os seguintes codigos no arquivo `<Microsoft.PowerShell_profile.ps1>` :

```
Import-Module posh-git
Import-Module oh-my-posh
Set-PoshPrompt -Theme <<nome_do_tema>>
$ThemeSettings.Font = 'Cascadia Code Nerd Font, 12
```

Substitua `<nome_do_tema>` pelo nome do tema que você deseja usar. Para verificar a lista completa de temas disponíveis, execute o comando:`Get-PoshThemes`

Se o comando `Get-PoshThemes` não funcionar, verifique a lista completa de temas disponíveis na documentação do Oh-My-Posh em [Lista de Temas](https://ohmyposh.dev/docs/themes "Veja a lista completa de temas disponíveis no Oh-My-Posh")

## Criando um arquivo de tema personalizado

Se você quiser criar um tema personalizado para o Oh-My-Posh, crie um arquivo `theme.omp.json` (ou o nome que preferir) em sua máquina e insira dentro do arquivo o código de um dos temas presentes na lista de temas disponíveis na documentação do Oh-My-Posh.

oh-my-posh init pwsh --config ' ``<caminho-para-o-arquivo-theme.omp.json>`` | Invoke-Expression

Insira o comando acima em seu arquivo |Microsoft.PowerShell_profile.ps1| Substitua `<caminho-para-o-arquivo-theme.omp.json>` pelo caminho para o arquivo de tema personalizado em sua máquina .

Pronto! Agora você tem um prompt personalizado para o PowerShell com o Oh-My-Posh. Para abrir o arquivo de perfil do PowerShell, execute o comando:

`notepad $PROFILE ou Code $PROFILE`

O arquivo de perfil do PowerShell é um arquivo de script que é executado automaticamente quando o PowerShell é iniciado. Você pode usar esse arquivo para configurar o prompt do PowerShell e outros aspectos do seu ambiente de linha de comando.

</div></div></pre>
