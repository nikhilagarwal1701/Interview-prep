package com.runclub.runclub.controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

import com.runclub.runclub.dto.ClubDto;
import com.runclub.runclub.services.ClubService;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class ClubController {
    private ClubService clubService;

    public ClubController(ClubService clubService) {
        this.clubService = clubService;
    }

    @GetMapping("allClubs")
    public String getAllClubs(Model model) {
        List<ClubDto> clubs = clubService.findAllClubs();
        model.addAttribute("clubs", clubs);
        return "clubs-list";
    }
    
}
