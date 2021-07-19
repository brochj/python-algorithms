# Dependency Insversion

### https://www.youtube.com/watch?v=Kv5jhbSkqLE

## Evitando/Diminuir acoplamento

Quando temos uma `class` que está recebendo outra `class` como parâmetro isso implica em um acoplamento.

`def __init__(self, l: LightBulb)` no caso, por mais que isso já seja composição, ainda não é bom.

```python
class LightBulb:
    def turn_on(self): ...

    def turn_off(self): ...

class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self): ...

l = LightBulb()
switch = ElectricPowerSwitch(l)
```

Para arrumar isso, vamos subir um level de abstração criando uma interface (classe abstrata) entre `ElectricPowerSwitch` e `LightBulb`

## Como criar a classe abstrata
A ideia aqui é se perguntar se `ElectricPowerSwitch` só existe/funciona com `LightBulb`? A resposta que queremos é **NÃO**.

Um `ElectricPowerSwitch` pode ligar/desligar diversas coisas, não somente `LightBulb`.

### Como achar o nome para a classe abstrata
Uma vez que sabemos outros objetos que `ElectricPowerSwitch` pode controlar, vamos tentar **identificar o que eles têm em comum**.

Exemplos:
- Lâmpada
- Ventilador 
- Motor

#### O que esses três objetos têm em comum? (características em comum)
- São ligados na rede elétrica
- Podem estar ligado/desligado
- Podem ter sua potência alterada

Como lá no começo estávamos utilizando ligar/desligar a `LightBulb`, vamos partir dessa característica para nomear nossa class abstrata

>Algo que pode estar ligado e desligado é `Switchable`

```python
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
```

Se quisessemos utilizar a característica de ter a potência alterada

>Algo que pode alterar-se a potência é dimerizável, podemos usar `Dimmable`

## Agora `LightBulb` é uma implementação de `Switchable` 

```python
class LightBulb(Switchable):
    def turn_on(self): ...

    def turn_off(self): ...
```

```python
class Fan(Switchable):
    def turn_on(self): ...

    def turn_off(self): ...
```

```python
class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
```
```python
l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
```