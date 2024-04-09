package com.runclub.runclub.dto;

import java.time.LocalDateTime;

import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "club")
public class ClubDto {
    private Long id;
    private String title;
    private String photoUrl;
    private String content;
    private LocalDateTime createdOn;
    private LocalDateTime updatedOn;

}
