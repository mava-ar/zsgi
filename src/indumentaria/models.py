from django.db import models

from core.models import Operarios


class Epp(models.Model):
    """
    ok
    """
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=45)
    medida = models.CharField(db_column='MEDIDA', max_length=45)

    class Meta:
        db_table = 'epp'
        verbose_name = "indumentaria"
        verbose_name_plural = "indumentaria"

    def __str__(self):
        return "{} {}".format(self.nombre, self.medida)


class EppEntrega(models.Model):
    """
    OK
    """
    id = models.AutoField(db_column='ID', primary_key=True)
    fecha = models.DateField(db_column='FECHA')
    observaciones = models.TextField(db_column='OBSERVACIONES', blank=True, null=True)
    operarioid = models.ForeignKey(Operarios, db_column='operarioId', null=True)

    class Meta:
        db_table = 'epp_entrega'
        verbose_name = "entrega de indumentaria"
        verbose_name_plural = "entregas de indumentaria"

    def __str__(self):
        return self.id
        # return "{} {}".format(self.fecha, self.operario.nombre)


class EppOperarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    epp = models.ForeignKey(Epp, db_column='EPP_ID')
    operario = models.ForeignKey(Operarios, db_column='OPERARIO_ID')
    valor = models.CharField(db_column='VALOR', max_length=128, blank=True, null=True)
    tipo = models.IntegerField(db_column='TIPO')

    class Meta:
        db_table = 'epp_operarios'
        verbose_name = "dato de indumentario de operario"
        verbose_name_plural = "datos de indumentaria de operarios"

    def __str__(self):
        return "{} {} ({} {})".format(self.valor, self.tipo, self.epp.nombre, self.operario.nombre)


class EppEntregaItem(models.Model):
    """
    OK
    """
    id = models.AutoField(db_column='ID', primary_key=True)
    epp_entrega = models.ForeignKey(EppEntrega, db_column='EPP_ENTREGA_ID')
    medida = models.CharField(db_column='MEDIDA', max_length=45)
    epp = models.ForeignKey(Epp, blank=True, null=True)

    class Meta:
        db_table = 'epp_entrega_item'
        verbose_name = "ítem de entrega de indumentaria"
        verbose_name_plural = "ítems entregas de indumentaria"

    def __str__(self):
        return "{}".format(self.medida)
