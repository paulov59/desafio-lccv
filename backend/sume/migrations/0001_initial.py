# Generated by Django 3.2.9 on 2021-12-12 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosBem',
            fields=[
                ('id_estado_bem', models.AutoField(primary_key=True, serialize=False)),
                ('estado_bem', models.CharField(choices=[('BOM', 'Bom'), ('REGULAR', 'Regular'), ('PRECÁRIO', 'Precario'), ('ANTIECONÔMICO', 'Antieconomico'), ('INSERSÍVEL', 'Inservivel')], max_length=80)),
                ('descricao', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Estado do Bem',
                'db_table': 'EstadosBem',
                'ordering': ['estado_bem'],
            },
        ),
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=60)),
                ('cnpj', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=12, null=True)),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Fornecedores',
                'db_table': 'Fornecedores',
                'ordering': ['razao_social'],
            },
        ),
        migrations.CreateModel(
            name='NaturezasDespesa',
            fields=[
                ('id_natureza_despesa', models.AutoField(primary_key=True, serialize=False)),
                ('cod_natureza_despesas', models.CharField(max_length=8)),
                ('desc_natureza_despesa', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Naturezas Despesas',
                'db_table': 'NaturezasDespesa',
                'ordering': ['desc_natureza_despesa'],
            },
        ),
        migrations.CreateModel(
            name='SitucoesUsoBem',
            fields=[
                ('id_situacao_uso_bem', models.AutoField(primary_key=True, serialize=False)),
                ('situacao_uso_bem', models.CharField(choices=[('EM USO', 'Emuso'), ('EM CAUTELA', 'Cautela'), ('EM MANUTENÇÂO', 'Manutencao'), ('EM DISPONIBILIDADE', 'Disponivel'), ('AGUARDANDO RECOLHIMENTO', 'Aguardandorecolhimento'), ('RECOLHIDO', 'Recolhido')], max_length=80)),
                ('descricao', models.CharField(max_length=255)),
                ('ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Situações de Uso',
                'db_table': 'SituacoesUsoBem',
                'ordering': ['situacao_uso_bem'],
            },
        ),
        migrations.CreateModel(
            name='NotasFiscais',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_nota_fiscal', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('id_fornecedor', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.fornecedores')),
                ('id_natureza_despesa', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.naturezasdespesa')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notasfiscais_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notasfiscais_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notas Fiscais',
                'db_table': 'NotasFiscais',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=80)),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marcas_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marcas_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'db_table': 'Marcas',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='ItensNotaFiscal',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_item_nota_fiscal', models.AutoField(primary_key=True, serialize=False)),
                ('qtd', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('produto_servico', models.CharField(max_length=100)),
                ('vinculado', models.BooleanField(default=True)),
                ('id_nota_fiscal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sume.notasfiscais')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itensnotafiscal_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itensnotafiscal_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Itens das notas fiscais',
                'db_table': 'ItensNotaFiscal',
                'ordering': ['produto_servico'],
            },
        ),
        migrations.CreateModel(
            name='Bens',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_bem', models.AutoField(primary_key=True, serialize=False)),
                ('tombamento', models.CharField(max_length=10)),
                ('valor_aquisicao', models.FloatField()),
                ('data_lim_garantia', models.DateField()),
                ('data_fim_garantia', models.DateField()),
                ('data_inicio_uso', models.DateField()),
                ('observacoes', models.TextField()),
                ('id_estado_bem', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.estadosbem')),
                ('id_item_nota_fiscal', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.itensnotafiscal')),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.marcas')),
                ('id_situacao_uso_bem', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='sume.situcoesusobem')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bens_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bens_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Itens das notas fiscais',
                'db_table': 'Bens',
                'ordering': ['tombamento'],
            },
        ),
    ]
