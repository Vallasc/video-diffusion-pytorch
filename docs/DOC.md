# Model structure
```fs
GaussianDiffusion(
  (denoise_fn): Unet3D(
    (time_rel_pos_bias): RelativePositionBias(
      (relative_attention_bias): Embedding(32, 8)
    )
    (init_conv): Conv3d(3, 64, kernel_size=(1, 7, 7), stride=(1, 1, 1), padding=(0, 3, 3))
    (init_temporal_attn): Residual(
      (fn): PreNorm(
        (fn): EinopsToAndFrom(
          (fn): Attention(
            (rotary_emb): RotaryEmbedding()
            (to_qkv): Linear(in_features=64, out_features=768, bias=False)
            (to_out): Linear(in_features=256, out_features=64, bias=False)
          )
        )
        (norm): LayerNorm()
      )
    )
    (time_mlp): Sequential(
      (0): SinusoidalPosEmb()
      (1): Linear(in_features=64, out_features=256, bias=True)
      (2): GELU()
      (3): Linear(in_features=256, out_features=256, bias=True)
    )
    (downs): ModuleList(
      (0): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(64, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=64, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=64, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): Conv3d(64, 64, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (1): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=256, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(64, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(64, 128, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=256, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(128, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=128, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=128, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): Conv3d(128, 128, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (2): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=512, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(128, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(128, 256, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=512, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(256, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=256, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=256, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): Conv3d(256, 256, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (3): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=1024, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(256, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(256, 512, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=1024, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(512, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=512, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=512, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): Identity()
      )
    )
    (ups): ModuleList(
      (0): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=512, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(1024, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(1024, 256, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=512, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 256, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(256, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=256, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=256, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): ConvTranspose3d(256, 256, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (1): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=256, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(512, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(512, 128, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=256, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 128, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(128, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=128, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=128, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): ConvTranspose3d(128, 128, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (2): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(256, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(256, 64, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(64, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=64, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=64, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): ConvTranspose3d(64, 64, kernel_size=(1, 4, 4), stride=(1, 2, 2), padding=(0, 1, 1))
      )
      (3): ModuleList(
        (0): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(128, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Conv3d(128, 64, kernel_size=(1, 1, 1), stride=(1, 1, 1))
        )
        (1): ResnetBlock(
          (mlp): Sequential(
            (0): SiLU()
            (1): Linear(in_features=256, out_features=128, bias=True)
          )
          (block1): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (block2): Block(
            (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
            (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
            (act): SiLU()
          )
          (res_conv): Identity()
        )
        (2): Residual(
          (fn): PreNorm(
            (fn): SpatialLinearAttention(
              (to_qkv): Conv2d(64, 768, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (to_out): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1))
            )
            (norm): LayerNorm()
          )
        )
        (3): Residual(
          (fn): PreNorm(
            (fn): EinopsToAndFrom(
              (fn): Attention(
                (rotary_emb): RotaryEmbedding()
                (to_qkv): Linear(in_features=64, out_features=768, bias=False)
                (to_out): Linear(in_features=256, out_features=64, bias=False)
              )
            )
            (norm): LayerNorm()
          )
        )
        (4): Identity()
      )
    )
    (mid_block1): ResnetBlock(
      (mlp): Sequential(
        (0): SiLU()
        (1): Linear(in_features=256, out_features=1024, bias=True)
      )
      (block1): Block(
        (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
        (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
        (act): SiLU()
      )
      (block2): Block(
        (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
        (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
        (act): SiLU()
      )
      (res_conv): Identity()
    )
    (mid_spatial_attn): Residual(
      (fn): PreNorm(
        (fn): EinopsToAndFrom(
          (fn): Attention(
            (to_qkv): Linear(in_features=512, out_features=768, bias=False)
            (to_out): Linear(in_features=256, out_features=512, bias=False)
          )
        )
        (norm): LayerNorm()
      )
    )
    (mid_temporal_attn): Residual(
      (fn): PreNorm(
        (fn): EinopsToAndFrom(
          (fn): Attention(
            (rotary_emb): RotaryEmbedding()
            (to_qkv): Linear(in_features=512, out_features=768, bias=False)
            (to_out): Linear(in_features=256, out_features=512, bias=False)
          )
        )
        (norm): LayerNorm()
      )
    )
    (mid_block2): ResnetBlock(
      (mlp): Sequential(
        (0): SiLU()
        (1): Linear(in_features=256, out_features=1024, bias=True)
      )
      (block1): Block(
        (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
        (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
        (act): SiLU()
      )
      (block2): Block(
        (proj): Conv3d(512, 512, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
        (norm): GroupNorm(8, 512, eps=1e-05, affine=True)
        (act): SiLU()
      )
      (res_conv): Identity()
    )
    (final_conv): Sequential(
      (0): ResnetBlock(
        (block1): Block(
          (proj): Conv3d(128, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
          (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
          (act): SiLU()
        )
        (block2): Block(
          (proj): Conv3d(64, 64, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1))
          (norm): GroupNorm(8, 64, eps=1e-05, affine=True)
          (act): SiLU()
        )
        (res_conv): Conv3d(128, 64, kernel_size=(1, 1, 1), stride=(1, 1, 1))
      )
      (1): Conv3d(64, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1))
    )
  )
)
```